# Cloudshell Demo
Cloudshell is a free, serverless interactive environment for interacting with GCP resources

1.  Create GCP Project:
    1.  Browse to https://console.cloud.google.com/
    2.  Create new project 
   
    ![Create New](https://user-images.githubusercontent.com/39421615/59232516-922a1780-8b99-11e9-9645-8a4b73328432.png)
   
    3.  Enable billing! $300 credit for new accounts.

    ![2019-06-10_16-07-37](https://user-images.githubusercontent.com/39421615/59232595-e92fec80-8b99-11e9-9bda-bcdc23d4b980.png)

    4. Enable APIs:
       1. Google Container Registry API

2. Cloudshell:
   1. Start a cloudshell session by clicking the icon
   
   ![2019-06-10_16-14-00](https://user-images.githubusercontent.com/39421615/59232808-c6ea9e80-8b9a-11e9-8636-73561461ff01.png)

   `git clone https://github.com/rojopolis/managed-ml.git`
   Update .cloudshellcustomimagerepo.json with project and image name
   `cloudshell env build-local` 
   `cloudshell env push`
   `cloudshell env update-default-image`
   Restart Cloudshell VM

   ![2019-06-10_17-29-58](https://user-images.githubusercontent.com/39421615/59235335-775da000-8ba5-11e9-80a1-0d445e904020.png)