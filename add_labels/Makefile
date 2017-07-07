bucket = cleveland-metroparks-trail-cam-images
dataDir = data
rawDir = $(dataDir)/raw
labelDir = $(dataDir)/labeled

labelFile = $(rawDir)/labels/FalseTriggers.species.metadata2.csv

dirs = $(dataDir) $(rawDir) $(labelDir)

label: label_data.py
	python3 label_data.py $(rawDir) $(labelDir) $(labelFile)

syncRaw:
	aws s3 sync s3://$(bucket)/ $(rawDir) --region=us-east-2

syncLabeled:
	aws s3 sync $(labelDir) s3://$(bucket)/labeled/ --region=us-east-2

$(dirs):
	mkdir -p $@
