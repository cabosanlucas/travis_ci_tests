echo "hi"
ls
git checkout master compute_metrics.py
python compute_metrics.py
git add .
git commit -m "adding feedback"
git push
