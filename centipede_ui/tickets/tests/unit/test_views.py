from mock import Mock, patch
from nose.tools import assert_equal

from centipede_ui.tickets.views import view_ticket


@patch('centipede_ui.tickets.views.settings.CENTIPEDE_URL', 'MockURL')
@patch('centipede_ui.tickets.views.render_to_response')
@patch('centipede_ui.tickets.views.Centipede')
def test_view_ticket(centipede, render_to_response):
    centipede.return_value.get_ticket.return_value = {
        'title': 'MockTitle',
        'description': 'MockDescription',
        'owner': 'MockOwner',
        'state': 'MockState',
        }
    ret = view_ticket(Mock(), 'US123')
    assert_equal([(('MockURL',), {})], centipede.call_args_list)
    assert_equal([(('US123',), {})],
                 centipede.return_value.get_ticket.call_args_list)
    assert_equal([(('tickets/view.html',
                    centipede.return_value.get_ticket.return_value), {})],
                 render_to_response.call_args_list)
    assert_equal(render_to_response.return_value, ret)
