import requests

class PyOpenFisheries(object):
    def __init__(self, **kwargs):
        self.landings = kwargs.get('landings')
        self.species = kwargs.get('species')
        self.country = kwargs.get('country')
        self.start_year = kwargs.get('start_year')
        self.end_year = kwargs.get('end_year')

    def annual_landings(self, species=None, country=None):
        """
            Gathers annual fishery landings filtered by either species or
            country. If neither fish nor country are specified, then this
            will return global aggregate landings data.

            Args:
                species: three-letter ASFIS species code (i.e. "SKJ" - Skipjack Tuna)
                country: ISO-3166 alpha 3 country code (i.e. "USA" - United States)

            Returns:
                instance: PyOpenFisheries instance with landings populated
        """

        url = "http://openfisheries.org/api/landings/"
        if ((species is not None) &  (country is not None)):
            return False
        else:
            if species:
                url += ("species/" + species + ".json" )
                r = requests.get(url)
                return PyOpenFisheries(landings = r.json(), species = species)
            elif country:
                url += ("countries/" + country + ".json")
                r = requests.get(url)
                return PyOpenFisheries(landings = r.json(), country = country)

    def filter_years(self, start_year=1950,end_year=2018):
        """
            Filters annual fishing data to within a time-frame.

            Args:
                start_year: 4 digit integer year (i.e. 1980)
                end_year: I 4 digit integer year (i.e. 2015)

            Returns:
                instance: PyOpenFisheries instance with years filtered.
        """

        filtered_landings = [landing for landing in self.landings if (
                landing['year'] >= start_year and landing['year'] <= end_year)]

        return PyOpenFisheries(
            landings = filtered_landings,
            species = self.species,
            country = self.country,
            start_year = start_year,
            end_year = end_year)

    def summarize(self):
        """ Summarizes what has been returned from OpenFisheries """
        base_string = "Landings of "
        if self.landings:
            if self.species:
                base_string += (self.species + " globally")
            elif self.country:
                base_string += ("all species in " + self.country)
            base_string += (" from " + str(self.start_year) + " to " + str(self.end_year))
            return base_string

        else:
            return "PyOpenFisheries API Wrapper"
