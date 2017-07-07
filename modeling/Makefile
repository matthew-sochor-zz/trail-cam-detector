
# define directories
data = data
rawDir = $(data)/raw
test = $(rawDir)/test
train = $(rawDir)/train
plotDir = $(data)/plots

imgSource = ../add_labels/data/labeled

dirs = $(data) $(rawDir) $(test) $(train) $(plotDir)

s3dir = cleveland-metroparks-trail-cam-images
testS3key = test/
trainS3key = train/

labelDirs = $(shell ls $(imgSource))

percent = 0.7

# Modeling

predict: predict.py
	python predict.py

model: train_head.py
	python train_head.py

features: imgs_to_arr.py arrs_to_aug.py arrs_to_emb.py | $(dirs)
	python imgs_to_arr.py
	python arrs_to_aug.py
	python arrs_to_emb.py

# Data
pullData: | $(dirs)
	aws s3 sync s3://$(s3dir)/$(testS3key) $(test) --region=us-east-2
	aws s3 sync s3://$(s3dir)/$(trainS3key) $(train) --region=us-east-2

clean:
	rm -rf $(data)

$(dirs):
	mkdir -p $@

reset_test_train:
	rm -rf $(test)
	rm -rf $(train)
	mkdir -p $(test)
	mkdir -p $(train)

$(labelDirs): reset_test_train
	mkdir -p $(test)/$@
	mkdir -p $(train)/$@
	python split.py $@ $(imgSource) $(test) $(train) $(percent)

# Terraform deployment 
start:
	terraform apply

connect:
	terraform refresh
	ssh -A -L 8888:localhost:8888 ubuntu@$(shell terraform output ip)

stop:
	terraform destroy

# Split data
split: $(labelDirs)
	@echo split

pushSplits:
	aws s3 sync $(train) s3://$(s3dir)/train 
	aws s3 sync $(test) s3://$(s3dir)/test 

pullSplits:
	aws s3 sync s3://$(s3dir)/train $(train)
	aws s3 sync s3://$(s3dir)/test $(test)