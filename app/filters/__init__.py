from datetime import date, datetime
from app import app, models
import calendar

@app.template_filter('format_timestamp')
def format_timestamp(value, format='matchtime'):
    if format == 'matchtime':
        # yyyy mm dd hh mm ss
        value = value.encode('ascii').split('.')
        return "{} {} {}:{}".format(calendar.month_name[int(value[1])], int(value[3]), int(value[3]), value[4] )
    if format == 'shortmatchtime':
        value = value.encode('ascii').split('.')
        return "{}/{} {}:{}".format(int(value[1]), int(value[3]), int(value[3]), value[4] )

@app.template_filter('obj_successfail')
def obj_successfail(succeeded):
    if succeeded:
        return "<span class='objective success'>Success</span>"
    else:
        return "<span class='objective failure'>Failure</span>"

@app.template_filter('obj_pretty')
def obj_pretty(objective):
    '''Makes antag objectives pretty for template views'''
    if objective.objective_type == u'/datum/objective/assassinate':
        return 'Asassinate {} the {}.'.format(objective.target_name, objective.target_role)
    else:
        return objective.objective_desc