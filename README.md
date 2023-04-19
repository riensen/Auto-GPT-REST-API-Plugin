# Auto-GPT REST API Plugin

## 🚀 Installation

Follow these steps to configure the Auto-GPT REST API Plugin:

### 1. Clone the Auto-GPT-REST-API-Plugin repository
Clone this repository and navigate to the `Auto-GPT-REST-API-Plugin` folder in your terminal:

```bash
git clone https://github.com/riensen/Auto-GPT-REST-API-Plugin.git
```

### 2. Install required dependencies
Execute the following command to install the necessary dependencies:

```bash
pip install -r requirements.txt
```

### 3. Package the plugin as a Zip file
Compress the `Auto-GPT-REST-API-Plugin` folder or [download the repository as a zip file](https://github.com/riensen/Auto-GPT-REST-API-Plugin/archive/refs/heads/master.zip).

### 4. Install Auto-GPT
If you haven't already, clone the [Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT) repository, follow its installation instructions, and navigate to the `Auto-GPT` folder.

### 5. Copy the Zip file into the Auto-GPT Plugin folder
Transfer the zip file from step 3 into the `plugins` subfolder within the `Auto-GPT` repo.

### 6. Locate the `.env.template` file
Find the file named `.env.template` in the main `/Auto-GPT` folder.

### 7. Create and rename a copy of the file
Duplicate the `.env.template` file and rename the copy to `.env` inside the `/Auto-GPT` folder.

### 8. Edit the `.env` file
Open the `.env` file in a text editor. Note: Files starting with a dot might be hidden by your operating system.

### 9. Add REST API configuration settings
Append the following configuration settings to the end of the file:

```ini
################################################################################
### REST API
################################################################################


```