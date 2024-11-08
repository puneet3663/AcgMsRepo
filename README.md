
Navigate to Storage accounts.
In the upper left corner, click Create.
For Resource group, select the existing resource group.
For Storage account name, enter acgmsdatalake.
Leave the other settings at default, and click Next: Advanced.
For Hierarchical Namespace, ensure Enable hierarchical namespace is selected.
Leave the other settings at default, and click Review.
Click Create.
Once the deployment is complete, click Go to resource.
Create a Container Named taxidata in the Data Lake Account
In the left navigation menu, under Data storage, click Containers.
Click + Container.
In the New container menu that appears on the right, enter taxidata for Name.
Click Create.
Click on the taxidata container.
Click +Add Directory.
In the Add Directory menu that appears on the right, leave Raw as the Name, and click Save.
Repeat steps 6-7, but this time, name the directory Output.
Click on the Raw folder.
Click Upload.
Click Browse for files, and select the TaxiRides.csv file you downloaded earlier.
Click Upload.
Create an Azure Data Factory Instance
In the search bar at the top of the window, search for and select Data factories.
Click +Create.
For Resource group, select the existing resource group.
For Instance details > Name, enter AcgMsDataFactory.
Leave the other settings at default, and click Next.
Click Review + create.
Click Create.
Click Go to resource.
Click Launch studio.
Set Up a New Repository in GitHub
In a new browser tab, open the GitHub website. Log in to an existing GitHub account, or create a new GitHub account if necessary.
Note: For more information about setting up a GitHub account, visit the Signing up for a New GitHub Account page.

In the upper right corner of the page, click the + icon, and select New repository.
For Repository name, enter AcgMsRepo.
Ensure Public is selected, so anyone on the internet can see the repository.
Under Initialize this repository, select Add a README file.
Click Create repository.
Configure GitHub in Azure Data Factory
Navigate back to the Data factory browser tab.
In the left navigation menu, click on the Author icon.
In the upper left corner, click on the Data Factory dropdown menu, and select Set up code repository.
In the menu that appears on the right, click on the Repository type dropdown menu, and select GitHub.
Under GitHub repository owner, enter your GitHub handle.
Click Continue. Since you're logged in to your GitHub account in a separate window, the authentication has automatically been performed. If you're not logged in, you will have to log in and connect Data Factory to your account.
On the Configure a repository menu, ensure Select repository is selected.
For Repository name, select AcgMsRepo.
Click on the Collaboration branch dropdown menu, and select +Create new.
On the pop-up that appears, enter collaboration as the Branch name.
Click Create.
Leave Publish branch as adf_publish.
Leave the other settings at default, and click Apply.
For Working branch, ensure Collaboration is selected.
Click Save.
Save Changes to Collaboration Branch
In the Factory Resources menu on the left, click the + icon next to the filter.
Select Pipeline > Pipeline.
Expand the pipeline1 window.
In the left navigation menu, under Move and transform, select Copy data, and drag and drop it onto the canvas.
Click Validate; notice the properties are not filled, which means the pipeline is invalid.
Close out of the Pipeline validation output window that appears on the right.
Click Save.
Navigate to your GitHub browser tab; ensure you're in the collaboration branch.
Click on the pipeline folder; notice the pipeline1.json file.
Navigate back to the Data factory browser tab.
Enter Source Properties
Click on the Source tab.
Next to Source dataset, click +New.
Under Select a data store, enter and select Azure Data Lake Storage Gen2.
Click Continue.
Select DelimitedText.
Click Continue.
For Set properties, enter the following:
Linked service: Select +New.
For Storage account name, select acgmsdatalake.
Click Create.
Next to File path, click on the folder icon, and select taxidata.
Select Raw.
Select TaxiRides.csv.
For Name, enter TaxiRidesCsvDataset.
Click OK.
Enter Sink Properties
Click on the Sink tab.
Next to Sink dataset, click +New.
Under Select a data store, enter and select Azure Data Lake Storage Gen2.
Click Continue.
Select Parquet.
Click Continue.
For Set properties, enter the following:
Linked service: Select AzureDataLakeStorage1.
Next to File path, click on the folder icon, and select taxidata.
Select Output.
For File path > File name, enter TaxiRides.parquet.
Under Import schema, select None.
For Name, enter TaxiRidesParquetDataset.
Click OK.
At the top of the page, click Validate; your pipeline should be successfully validated.
Close out of the Pipeline validation output window that appears on the right.
Click Save.
Publish the Changes to Publish Branch
At the top of the page, next to collaboration branch, click Publish.
Click OK to close out of the Pending changes window that appears on the right.
Once the publishing is complete, navigate back to your GitHub browser tab.
In the left navigation menu, click on the collaboration dropdown menu, and select View all branches.
Click on the adf_publish branch.
Select the AcgMsDataFactory folder.
Open the ARMTemplateForFactory.json file, and review it.
Conclusion
Congratulations — you've completed this hands-on lab!
