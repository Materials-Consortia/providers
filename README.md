<a href="https://www.optimade.org/"><img src="https://avatars0.githubusercontent.com/u/23107754" align="left" width="10%" ></a>

# OPTIMADE Providers Index Meta-Database

The list of providers is published as an [OPTIMADE](https://www.optimade.org/) Index Meta-Database here: [https://providers.optimade.org/](https://providers.optimade.org/)

You can obtain the list of providers in a machine-readable format following the [OPTIMADE specification for Index Meta-Databases](https://github.com/Materials-Consortia/OPTIMADE/blob/develop/optimade.rst#32index-meta-database) by using the following URL:

- [https://providers.optimade.org/v1/links](https://providers.optimade.org/v1/links)

where `v1` is currently the latest version and can be replaced with any major version name of the OPTIMADE specification.

For convenience, you can also access the most recent list of providers in the format mandated by the latest version of the OPTIMADE specification directly at this URL:

- [https://providers.optimade.org/providers.json](https://providers.optimade.org/providers.json)

You can contribute a new provider or amend the current information by creating a pull request to [the `providers` repository](https://github.com/Materials-Consortia/providers).


## Repository organization

The OPTIMADE providers repository is hosted here: [https://github.com/Materials-Consortia/providers](https://github.com/Materials-Consortia/providers)

The repository is organized this way:

- `/src/links/<version>/providers.json` is the current providers.json file formatted according to OPTIMADE version `<version>` and any later version that uses a format that is backward compatible with this version.

- `/src/info/<version>/info.json` is the proper response to the info endpoint formatted according to OPTIMADE version `<version>` and any later version that uses a format that is backward compatible with this version.

- `/_redirect` specify http rewrites to map index meta-database URLs `/<version>/info` and `/<version>/links` to the corresponding files under `src/`, as well as `/providers.json`.

- `/<version>` directories contain symlinks `info.html` and `links.html` to the corresponding files under `src/` to somewhat support hosting solutions that do not understand the instructions in `_redirect` but which support "pretty URLs".

- `/providers.json` is a symbolic link continously updated to point at the latest version of the providers.json file under `/src/` to somewhat support hosting solutions that do not understand the instructions in `_redirect`.

Presently, only the `v1` version of the formats exist.
Hence, to update the list of providers, file a pull-request against the repository to edit `/src/links/v1/providers.json`.

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
