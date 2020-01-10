immune_exposure.csv: convert.py immune_exposure.txt
	python3 $^ $@

immune_exposure.owl: immune_exposure_template.tsv
	bin/robot template \
	--prefix "IE: http://example.com/IE_" \
	--prefixes obo_context.jsonld \
	--template $< \
	--output $@

immune_exposure_report.txt: immune_exposure.csv immune_exposure.owl
	bin/robot validate --csv $(word 1,$^) --owl $(word 2,$^) --output $@

immune_exposure_report.xlsx: immune_exposure.csv immune_exposure.owl
	bin/robot validate --csv $(word 1,$^) --owl $(word 2,$^) --output $@
