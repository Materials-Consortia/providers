<a href="https://www.optimade.org/"><img src="https://avatars0.githubusercontent.com/u/23107754" align="left" width="10%" ></a>

# OPTIMADE Providers Index Meta-Database

The list of providers is published as an [OPTIMADE](https://www.optimade.org/) Index Meta-Database here: [https://providers.optimade.org/](https://providers.optimade.org/)

You can obtain the list of providers in a machine-readable format following the [OPTIMADE specification for Index Meta-Databases](https://github.com/Materials-Consortia/OPTIMADE/blob/master/optimade.rst#index-meta-database) by using the following URL:

- [https://providers.optimade.org/v1/links](https://providers.optimade.org/v1/links)

where `v1` is currently the latest version and can be replaced with any major version name of the OPTIMADE specification.

For convenience, you can also access the most recent list of providers in the format mandated by the latest version of the OPTIMADE specification directly at this URL:

- [https://providers.optimade.org/providers.json](https://providers.optimade.org/providers.json)

Additionally, there is a providers dashboard that includes the results of validation of listed implementations.
This can be accessed at the following URL:

- [https://optimade.org/providers-dashboard](https://optimade.org/providers-dashboard)

You can contribute a new provider or amend the current information by creating a pull request to [the `providers` repository](https://github.com/Materials-Consortia/providers).

## Repository organization

The OPTIMADE providers repository is hosted here: [https://github.com/Materials-Consortia/providers](https://github.com/Materials-Consortia/providers)

The repository is organized this way:

- `/src/links/<version>/providers.json` is the current providers.json file formatted according to OPTIMADE version `<version>` and any later version that uses a format that is backward compatible with this version.
  Contributors should edit this file when adding a new provider, and may also want to add an index-metadatabase (see below).

- `/src/index-metadbs/<provider_name>/<version>/info.json` and `/src/index-metadbs/<provider_name>/<version>/links.json` are static Index Meta-Databases that are hosted in this repository for those providers that only have one main sub-database (or very few sub-databases) and do not wish to maintain one on their own.
  See more details and instructions in [Index Meta-Database README](./src/index-metadbs/README.md).

- `/src/info/<version>/info.json` is the proper response to the info endpoint formatted according to OPTIMADE version `<version>` and any later version that uses a format that is backward compatible with this version.
  Contributors should NOT edit this file when adding a new provider.

- `/_redirects` specifies http rewrites to map index meta-database URLs `/<version>/info` and `/<version>/links` to the corresponding files under `src/`, as well as `/providers.json`.
  It also creates `/index-metadbs/<provider_name>/<version>/info.json` and `/index-metadbs/<provider_name>/<version>/links.json` URLs to point to the corresponding files in the `/src/index-metadbs` subfolders.
  This is used by the deploy tool Netlify.
  Contributors should NOT edit files in this directory when adding a new provider.

Presently, only the `v1` version of the formats exist.
Hence, to update the list of providers, file a pull-request against the repository to edit `/src/links/v1/providers.json`.

## Requirements to be listed in this providers list

It is a policy of this providers list ([providers.optimade.org](https://providers.optimade.org)) that links inside `providers.json` must be links to an [OPTIMADE Index Meta-Database](https://github.com/Materials-Consortia/OPTIMADE/blob/master/optimade.rst#index-meta-database).

If you only have one or few databases in your implementation, and you do not want to host an Index Meta-Database yourself, you can host the Index Meta-Database directly in this repository.
You can find instructions [here](./src/index-metadbs).

## Fork this repository to set up an index meta-database for your own databases

- Click on the Fork button in GitHub and follow the instructions.

- Edit `/src/info/v1/info.json` with your information:

  - Make sure to update the URL in `available_api_versions` to point at your hosting location.

- Copy the file `src/index-metadbs/exmpl/v1/links.json` to `/src/info/v1/links.json` and edit this template to supply information about your own databases.

- Edit `README.md` to say who you are and what databases you provide.

- Remove the directory 'src/static-index-metadbs'

- Configure your hosting provider to use your forked repository.
  The repository presently contains configuration files for Netlify, which you can set up as follows:

  - Deploy using the Netlify *Continuous Deployment: GitHub App* option, and give it access to your forked repository with the following settings:
  
    - Build commmand: `jekyll build`
    - Publish directory: `_site/`

  - You are also recommended to configure a subdomain in *Domain settings* at Netlify, or setup your own custom domain.

- If you are a provider of OPTIMADE databases and you have set up the index meta-database to point at them, please post a pull-request against [https://github.com/Materials-Consortia/providers](https://github.com/Materials-Consortia/providers) to add the URL for your index meta-database to the central OPTIMADE providers list.
