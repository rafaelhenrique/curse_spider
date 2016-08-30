clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name "*.zip" -type f | xargs rm -rf

run: clean
	scrapy crawl addons

extract:
	cd out/full && find . -iname "*.zip" -exec unzip -o {} \;

requirements:
	pip install -r requirements.txt
