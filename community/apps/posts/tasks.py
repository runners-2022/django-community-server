# Django
from celery import shared_task

# Gateway
from community.modules.gateways.post import gateway as gateway_post


# Main Section
@shared_task(name='sync_post_task', bind=True)
def sync_post_task(self, post_id):
    print('========================= Post: sync_post_task =========================')

    from community.apps.posts.api.serializers import PostSyncSerializer
    from community.apps.posts.models import Post

    post = Post.objects.filter(id=post_id).first()
    if not post:
        return

    data = PostSyncSerializer(instance=post).data

    # API Gateway
    gateway_post.sync_post(data)


@shared_task(name='delete_post_task', bind=True)
def delete_post_task(self, post_id):
    print('======================= Post Celery: delete_post_task =======================')

    # Models
    from community.apps.posts.models import Post

    # Serializers
    from community.apps.posts.api.serializers import PostDeleteSerializer

    post = Post.objects.get(id=post_id)
    data = PostDeleteSerializer(instance=post).data

    # API Gateway
    gateway_post.delete_post(data)
