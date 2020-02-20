<a href="https://www.optimade.org/"><img src="https://avatars0.githubusercontent.com/u/23107754" align="left" width="10%" ></a>

# OPTiMaDe Providers Index Meta-Database

The list of OPTiMaDe providers keeps track of all reserved database-specific prefixes and the URLs to the index databases of all OPTiMaDe database providers that participate in the [OPTiMaDe network](https://www.optimade.org/).

The list of providers is published in the form of a statically hosted OPTiMaDe Index Meta-Database here:

- [https://providers.optimade.org/](https://providers.optimade.org/)

If you specifically seek the current list of providers for the latest version of the OPTiMaDe specification, you can access it at this URL:

- [https://providers.optimade.org/providers.json](https://providers.optimade.org/providers.json)

If you seek the list of providers formatted according to a specific major version of the OPTiMaDe specification, you can access it using this URL:

- [https://providers.optimade.org/*\<version\>*/links](https://providers.optimade.org/v1/links)

Where `<version>` designates a major version name of the OPTiMaDe specification, e.g., `v1`. 

## Repository organization

The OPTiMaDe providers repository is hosted here: [https://github.com/Materials-Consortia/providers](https://github.com/Materials-Consortia/providers)

The repository is organized this way:

- `/src/links/<version>/providers.json` is the current providers.json file formatted according to OPTiMaDe version `<version>` and any later version that uses a format that is backward compatible with this version.

- `/src/info/<version>/info.json` is the proper response to the info endpoint formatted according to OPTiMaDe version `<version>` and any later version that uses a format that is backward compatible with this version.

- `/_redirect` specify http rewrites to map index meta-database URLs `/<version>/info` and `/<version>/links` to the corresponding files under `src/`, as well as `/providers.json`.

- `/<version>` directories contain symlinks `info.html` and `links.html` to the corresponding files under `src/` to somewhat support hosting solutions that do not understand the instructions in `_redirect` but which support "pretty URLs".

- `/providers.json` is a symbolic link continously updated to point at the latest version of the providers.json file under `/src/` to somewhat support hosting solutions that do not understand the instructions in `_redirect`.

Presently, only the `v1` version of the formats exist.
Hence, to update the list of providers, file a pull-request against the repository to edit `/src/links/v1/providers.json`.

## Fork this repository to set up an index meta-database for your own databases

- Click on the Fork button in GitHub and follow the instructions.

- Edit `/src/info/v1/info.json` with your information:

  - Make sure to update the URL in `available_api_versions` to point at your hosting location.

- Edit `/src/info/v1/info.json` to point out your OPTiMaDe databases:

  - Put all your databases on the form:
    ```
    {
      "type": "child",
      "id": "example_main",
      "attributes": {
        "name": "Example name",
        "description": "Example database containing example entries",
        "base_url": "https://www.example.com/optimade",
        "homepage": "https://www.example.com"
      }
    }
    ```

  - Include also the following segment:
    ```
    {
      "type": "parent",
      "id": "optimade_index",
      "attributes": {
        "name": "OPTiMaDe providers",
	"description": "OPTiMaDe index meta-database of known providers",
        "base_url": "https://providers.optimade.org",
        "homepage": "https://www.optimade.org"
      }
    }
    ```

- Edit `README.md` to say who you are and what databases you index.

- Configure your hosting provider to use your forked repository.
  The repository presently contains configuration files for Netlify, which you can set up as follows:

  - Deploy using the Netlify *Continuous Deployment: GitHub App* option, and give it access to your forked repository with the following settings:
  
    - Build commmand: `jekyll build`
    - Publish directory: `_site/`

  - You are also recommended to set something sane for your subdomain in *Domain settings*, or even setup your own custom domain.

- If you are a provider of OPTiMaDe databases and you have set up the index meta-database to point at them, please post a pull-request against [https://github.com/Materials-Consortia/providers](https://github.com/Materials-Consortia/providers) to add the URL for your index meta-database to the central OPTiMaDe providers list.
