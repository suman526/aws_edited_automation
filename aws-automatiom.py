import os
import getpass
import subprocess
import pyttsx3
while(True):
    def aws_menu():	
        os.system('cls')
        os.system('tput setaf 3')
        print("") 
        print("\t\t\t\t\tFOR AWS CONFIGURATION: ")
        os.system('tput setaf 5')
        print("PLEASE ENTER YOUR\n 1. IAM ACCESS KEY ID \n 2. ACCESS KEY \n 3. REGION \n 4. OUTPUT FORMAT \n ") 
        os.system("aws configure")
        print("\n\n \t\t\t\tAWS CONFIGURED!!")
        os.system("color 02")
        input("\n\nenter to continue............")
        while(True): 
            def ec2_menu():
                while(True):
                    os.system('cls')
                    os.system('tput setaf 7')
                    print("\t\t\t\tWELCOME TO EC-2 SERVICE !!")
                    print("\t\t\t\t**************************")
                    os.system('tput setaf 6')
                    print("""
                            PRESS 1:TO LAUNCH YOUR INSTANCE
                            PRESS 2:TO START YOUR INSTANCE
                            PRESS 3:To STOP YOUR INSTANCE
                            PRESS 4:TO DESCRIBE YOUR INSTANCES
                            PRESS 5:RETURN TO MAIN MENU
                            PRESS 6:TO EXIT
                            """)
                    choice = input("Enter your choice: ")
                    if choice == "1":
                        count=int(input("How many instance you want to launch:"))
                        ami= input("Enter the image id of the instance:- ")
                        subnet_id = input("Enter the subnet id : ")
                        instance_type= input("Enter the type of instance that you want to launch :")
                        key_name = input("Enter your keyname:")
                        security_group= input("Enter the security group id")
                        os.system("aws ec2 run-instances  --image-id {} --instance-type {} --count {} --subnet-id {} --key-name {} --security-group-ids {}".format(ami,instance_type,count,subnet_id,key_name,security_group))
                        print("\n\n\t\t Your Instance Launched!")
                        print("")
                        input("\n Enter to continue..............")
                    elif choice == "2":
                        instanceid = input("Enter your instance id :")
                        os.system("aws ec2 start-instances --instance-ids {}".format(instanceid))
                        input("\n Enter to continue..............")
                    elif choice == "3":
                        instanceid = input("Enter your instance id :")
                        os.system("aws ec2 stop-instances --instance-ids {}".format(instanceid))
                        input("\n Enter to continue..............")
                    elif choice == "4":
                        os.system("aws ec2 describe-instances")
                        os.system("color 02")
                        input("\n\n Enter to continue..............")
                    elif choice == "5":
                        return
                    else:
                        os.system('tput setaf 7')
                        exit()
            def key_pair_menu():
                while True:
                    os.system('cls')
                    os.system('tput setaf 7')
                    print("\t\t\t\t\t\t\tAWS KEY PAIR MENU ")
                    print("\t\t\t\t\t\t\t*******************")
                    os.system('tput setaf 6')
                    print("""
                                PRESS 1: TO CREATE KEY-PAIR
                                PRESS 2: TO DELETE KEY-PAIR
                                PRESS 3: TO DESCRIBE KEY-PAIR
                                PRESS 4: TO EXIT
                            """)
                    choice = input(" Enter your choice : ")
                    if choice == "1":
                        key_name = input("Enter Key-name: ")
                        os.system("aws ec2 create-key-pair --key-name {} --query KeyMaterial --output text >  {}".format(key_name,key_name))
                        input("\n Enter to continue..............")
                    elif choice == "2":
                        key_name = input("Enter Key-name")
                        os.system("aws ec2 delete-key-pair --key-name {}".format(key_name))
                        input("\n Enter to continue..............")
                    elif choice == "3":
                        os.system("aws ec2 describe-key-pairs")
                        input("\n Enter to continue..............")
                    else:
                        os.system('tput setaf 1')
                        print("You have typed something wrong!")
                        input("ARE YOU SURE YOU WANT TO EXIT!! \n Enter to continue..............")
                        return
            def security_Group_menu():
                while(True):
                    os.system('cls')
                    os.system('tput setaf 7')
                    print("\t\t\t\t\tWELCOME TO SECURITY GROUP MENU ")
                    print("\t\t\t\t\t*******************************")
                    os.system('tput setaf 3')
                    print("""
                            PRESS 1: TO CREATE SECURITY GROUP
                            PRESS 2: TO DELETE SECURITY GROUP
                            PRESS 3: TO DESCRIBE SECURITY GROUP
                            PRESS 4: TO EXIT
                        """)
                    choice = int(input("Enter your choice:"))
                    if choice == 1:
                        os.system("color 02")
                        des = input("Enter Description of security group : ")
                        gn = input("Enter security group Name : ")
                        os.system("aws ec2  create-security-group --description {} --group-name {}".format(des,gn))
                        input("\n Enter to continue..............")
                    elif choice == 2:
                        os.system("color 02")
                        id = input("Enter secirity group Id: ")
                        os.system(" aws ec2 delete-security-group --group-id {}".format(id))
                    elif choice == 3:
                        os.system("color 02")
                        os.system("aws ec2 describe-security-groups")
                        input("\n Enter to continue..............")
                    else:
                        os.system('cls')
                        return            
            def ebs_menu():
                while(True):
                    os.system('cls')
                    os.system('tput setaf 7')
                    print("\t\t\t\t\tAWS VOLUME MENU ")
                    print("\t\t\t\t\t****************")
                    os.system('tput setaf 5')
                    print("""
                            PRESS 1: TO CREATE VOLUME
                            PRESS 2: TO DELETE VOLUME
                            PRESS 3: TO ATTACH VOLUME
                            PRESS 4: TO DETACH VOLUME
                            PRESS 5: TO DESCRIBE VOLUME
                            PRESS 6: TO RETURN TO MAIN MENU
                        """)
                    choice=input("Enter your Choice: ") 
                    if choice == "1":
                        zone = input("Enter AZ : ")
                        size = input("size: ")
                        os.system("aws ec2 create-volume --availability-zone {} --size {}".format(zone,size))
                        input("\n Enter to continue..............")
                    elif choice == "2":
                        volume_id = input("Enter Volume ID : ")
                        os.system("aws ec2 delete-volume --volume-id {}".format(volume_id))
                        input("\n Enter to continue..............")
                    elif choice == "3":
                        device_name = input("Enter  device Name: ")
                        instance_id = input("Instance ID: ")
                        volume_id = input("Volume ID: ")
                        os.system("aws ec2 attach-volume --device {} --instance-id {} --volume-id {}".format(device_name,instance_id,volume_id))
                        input("\n Enter to continue..............")
                    elif choice == "4":
                        volume_id = input("Volume ID: ")
                        os.system("aws ec2 detach-volume --volume-id {} ".format(volume_id))
                        input("\n Enter to continue..............")
                    elif choice == "5":
                        os.system("color 02")
                        os.system("aws ec2 describe-volumes")
                        input("\n Enter to continue..............")
                    else:
                        os.system('tput setaf 7')
                        return
            def s3_menu():
                while(True):
                    os.system("cls")
                    os.system('tput setaf 7')
                    print("\t\t\t\tWELCOME TO S3 SERVICE !!")
                    print("\t\t\t\t************************")
                    os.system('tput setaf 4')
                    print('''
                            Press 1: FOR CREATING BUCKET
                            Press 2: FOR ADDING OBJECT(IMAGE/VIDEOS)
                            Press 3: FOR BUCKET LIST
                            Press 4: FOR DELETING BUCKET
                            Press 5: FOR DELETING OBJECT OF BUCKET
                            PRESS 6: TO RETURN TO MAIN MENU
                        ''')
                    choice=input("Enter your choice :")
                    if choice == "1":
                        bucket_name=input("ENTER BUCKET NAME: ")
                        region_s3=input("ENTER REGION: ")
                        os.system("aws s3api create-bucket --bucket {} --region {}".format(bucket_name,region_s3))
                        input("\n Enter to continue..............")
                    elif choice == "2":
                        bucket_name=input("\n ENTER BUCKET NAME: ")
                        obj_path= input("\t ENTER THE PATH OF THE OBJECT:")
                        name=input("ENTER THE NAME OF THE OBJECT:")
                        os.system("aws s3api put-object --bucket {} --key {} --body \"{}\"".format(bucket_name,key,obj_path))
                        input("ENTER TO CONTINUE.........")
                    elif choice == "3":
                        os.system('aws s3api list-buckets --query "Buckets[].Name"')
                        input("\n Enter to continue..............")
                    elif choice == "4":
                        bucket_name=input("\n ENTER BUCKET NAME: ")
                        region_name=input("\n ENTER REGION:")
                        os.system("aws s3api delete-bucket --bucket {bucket_name} --region {region_name}")
                    elif choice == "5":
                        bucket_name=input("\n ENTER BUCKET NAME: ")
                        object_name=input("\n ENTER OBJECT NAME: ")
                        os.system("aws s3 rm s3://{bucket}/{object}".format(bucket=bucket_name,object=object_name))
                        input("\n Enter to continue..............")
                    else:
                        return           
            def cloudFront_menu():
                while(True):
                    os.system("cls")
                    os.system('tput setaf 10')
                    print("\t\t\t\t\t\t WELCOME TO CLOUD FRONT DISTRIBUTION ")
                    print("\t\t\t\t\t\t*************************************")
                    os.system('tput setaf 6')
                    print('For creating cloud front distribution;Enter some required details')
                    bucketname=input("\nENTER BUCKET NAME:")
                    objectname=input("\nENTER OBJECT NAME:")
                    os.system("aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com --default-root-object {}".format(bucketname,objectname))
                    input("ENTER TO CONTINUE..............")
            os.system('clear')
            os.system('tput setaf 7')
            print("\t\t\t\t\t\t\tAWS MENU DRIVEN ")
            print("\t\t\t\t\t\t\t****************")
            os.system('tput setaf 6')
            print("""
                    Press 1: FOR CREATING YOUR KEY PAIR
                    Press 2: FOR SECURITY-GROUP SERVICES	
                    Press 3: FOR EC2 SERVICES
                    Press 4: FOR EBS SERVICES
                    Press 5: FOR S3 SERVICES
                    Press 6: FOR CLOUD FRONT DISTRIBUTION SERVICES
                    Press 7: FOR RETURNING TO MAIN MENU
                """)
            choice = int(input("\n Enter Your Choice:\t"))
            if choice == 1:
                key_pair_menu()
            elif choice == 2:
                security_Group_menu()
            elif choice == 3:
                ec2_menu()
            elif choice == 4:
                ebs_menu()
            elif choice == 5:
                s3_menu()
            elif choice == 6:
                cloudFront_menu()
            else:
                return
    os.system("clear")
    os.system('tput setaf 7')
    print("\t\t\t\t\tAWS COMMAND LINE INTERFACE!")
    print("\t\t\t\t\t***************************")
    os.system('tput setaf 3')
    print("""
                Press 1:  FOR ENTERING YOUR AWS CLOUD WORLD	   
             """)
    os.system('tput setaf 7')
    choice = int(input("\n Enter Your Choice:"))
    if choice == 1:
        aws_menu()
    else:
        exit()
    









   
        

