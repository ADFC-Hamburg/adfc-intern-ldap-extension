# -*- coding: utf-8 -*-
from univention.admin.syntax import select


class ADFCLvSyntax(select):
    """
    ADFC Landesverbände
    """
    choices = [
        ('Baden-Wuertenberg', 'Baden-Württemberg'),
        ('Bayern', 'Bayern'),
        ('Berlin','Berlin'),
        ('Brandenburg','Brandenburg'),
        ('Bremen','Bremen'),
        ('Hamburg','Hamburg'),
        ('Hessen','Hessen'),
        ('Mecklenburg-Vorpommern','Mecklenburg-Vorpommern'),
        ('Niedersachsen','Niedersachsen'),
        ('Nordrhein-Westfalen','Nordrhein-Westfalen'),
        ('Rheinland Pfalz','Rheinland Pfalz'),
        ('Saarland','Saarland'),
        ('Sachsen','Sachsen'),
        ('Sachsen-Anhalt','Sachsen-Anhalt'),
        ('Schleswig-Holstein','Schleswig-Holstein'),
        ('Thueringen','Thüringen')
    ]