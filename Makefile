all:
	python .gen.py

pages:
	git checkout pages
	find ./ -type f -name "*.md" -print | xargs -i sed -i '1 s/^/\xef\xbb\xbf&/' {}
	git add ./
	git commit -m "pages"
	git push origin pages:pages