.PHONY: extract requirements validate replace

immune_exposure.csv: convert.py immune_exposure.txt
	python3 $^ $@

tables:
	mkdir -p $@

requirements:
	pip install -r requirements.txt

extract: tables requirements
	xlsx2csv -a -d tab immune_exposure.xlsx $<
	for f in tables/*.csv ; do \
	  		mv $$f "$${f%.csv}.tsv"; \
	  done

report.tsv: tables requirements
	valve $< -o $@

validate:
	make report.tsv
