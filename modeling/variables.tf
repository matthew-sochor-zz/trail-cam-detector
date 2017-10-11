variable "key_pair"{
	type = "string"
	default = "sochor"
}

variable "ami" {
	type = "string"
	default = "ami-e9c0e18c"
}

variable "spot_price" {
	type = "string"
	default = "0.40"
}

variable "profile" {
	type = "string"
	default = "Modeler"
}

variable "subnet" {
	type = "string"
	default = "subnet-6347d50a"
}

# These allow Josiah home, Sochor home and prog network IPs ssh access
variable "security_groups" {
	type = "list"
	default = ["sg-531f533a", "sg-a51d51cc", "sg-c11c50a8", "sg-2438294d"] 
}

variable "volume_type" {
	type = "string"
	default = "gp2"
}

variable "volume_size" {
	type = "string"
	default = "256"
}

variable "region" {
	type = "string"
	default = "us-east-2"
}

variable "instance_type" {
	type = "string"
	default = "p2.xlarge"
}
