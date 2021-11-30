from tethys_sdk.base import TethysAppBase, url_map_maker


class NationalWaterLevelForecastColombia(TethysAppBase):
    """
    Tethys app class for National Water Level Forecast Colombia.
    """

    name = 'National Water Level Forecast Colombia'
    index = 'national_water_level_forecast_colombia:home'
    icon = 'national_water_level_forecast_colombia/images/icon.gif'
    package = 'national_water_level_forecast_colombia'
    root_url = 'national-water-level-forecast-colombia'
    color = '#8e44ad'
    description = ''
    tags = '"Hydrology", "Time Series" "Water Level", "Colombia", "GEOGLowS"'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='national-water-level-forecast-colombia',
                controller='national_water_level_forecast_colombia.controllers.home'
            ),
        )

        return url_maps