resource "aws_instance" "my_public_server" {
  ami                    = data.aws_ami.aws_basic_linux.id
  instance_type          = var.ec2_type
  subnet_id              = data.aws_subnet.public.id
  vpc_security_group_ids = [aws_security_group.my_public_app_sg.id]
  key_name               = var.my_keypair
}

resource "aws_instance" "my_private_server"{
  count = var.number_of_instances
  ami                   = data.aws_ami.aws_basic_linux.id
  instance_type         = var.ec2_type
  subnet_id             = data.aws_subnet.private.id
  vpc_security_group_ids = [aws_security_group.my_private_app_sg.id]
  key_name              = var.my_keypair

   tags = {
      Name = "private_server_${count.index + 1}"
  }
}