# Terraform deployment 
start:
	terraform apply

connect:
	terraform refresh
	ssh -A -L 8888:localhost:8888 ubuntu@$(shell terraform output ip)

stop:
	terraform destroy