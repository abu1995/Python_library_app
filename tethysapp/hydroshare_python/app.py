from tethys_sdk.base import TethysAppBase, url_map_maker


class HydrosharePython(TethysAppBase):
    """
    Tethys app class for Hydroshare library.
    """

    name = 'Hydroshare library'
    index = 'hydroshare_python:home'
    icon = 'hydroshare_python/images/icon.gif'
    package = 'hydroshare_python'
    root_url = 'hydroshare-python'
    color = '#330033'
    description = '"An app which has the basic functions of the Hydroshare python client library"'
    tags = 'Python library, Hydroshare'
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
                url='hydroshare-python',
                controller='hydroshare_python.controllers.home'
            ),
            UrlMap(
                name='get_file',
                url='hydroshare-python/get_file',
                controller='hydroshare_python.controllers.get_file'
            ),
            UrlMap(
                name='add_file',
                url='hydroshare-python/add_file',
                controller='hydroshare_python.controllers.add_file'
            ),
            UrlMap(
                name='delete_resource',
                url='hydroshare-python/delete_resource',
                controller='hydroshare_python.controllers.delete_resource'
            ),
            UrlMap(
                name='delete_file',
                url='hydroshare-python/delete_file',
                controller='hydroshare_python.controllers.delete_file'
            ),
            
        )

        return url_maps