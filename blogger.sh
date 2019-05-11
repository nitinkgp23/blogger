#/bin/bash

echo Enter filename of the blog
read var

python /Users/nitinchoudhary/Projects/Blogger/blogger.py $var
echo Pushing to Github!

cd /Users/nitinchoudhary/Projects/nitinkgp23.github.io
git add .
git commit -m "Adding new blog post"
git push origin master