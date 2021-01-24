from main.models import Post
import datetime

p = Post(post_date=datetime.date.today(), post_author='Chandler')
p.save()
print(p)
resume = Post.objects.create(post_date=datetime.date.today(), post_author='Monica')
print(resume)
resume2 = Post.objects.create(post_date=datetime.date.today(), post_author='Phoebe')
print(resume2)

if Post.objects.filter(post_date__year=2021):
    print(f"new entries found, {Post.objects.count()} pcs")