from django.db import models

class Hashvaa(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=25)
    title = models.CharField(max_length=128)
    
    # Hospital fields
    איכילוב = models.CharField(max_length=512, null=True, blank=True, db_column='איכילוב', verbose_name="איכילוב")
    תל_השומר_שיבא = models.CharField(max_length=512, null=True, blank=True, db_column='תל השומר שיבא', verbose_name="תל השומר שיבא")
    לניאדו = models.CharField(max_length=512, null=True, blank=True, db_column='לניאדו', verbose_name="לניאדו")
    מאיר = models.CharField(max_length=512, null=True, blank=True, db_column='מאיר', verbose_name="מאיר")
    קפלן = models.CharField(max_length=512, null=True, blank=True, db_column='קפלן', verbose_name="קפלן")
    מעייני_הישועה = models.CharField(max_length=512, null=True, blank=True, db_column='מעייני הישועה', verbose_name="מעייני הישועה")
    אסף_הרופא = models.CharField(max_length=512, null=True, blank=True, db_column='אסף הרופא', verbose_name="אסף הרופא")
    וולפסון = models.CharField(max_length=512, null=True, blank=True, db_column='וולפסון', verbose_name="וולפסון")
    בלינסון = models.CharField(max_length=512, null=True, blank=True, db_column='בלינסון', verbose_name="בלינסון")
    עין_כרם = models.CharField(max_length=512, null=True, blank=True, db_column='עין כרם', verbose_name="עין כרם")
    שערי_צדק = models.CharField(max_length=512, null=True, blank=True, db_column='שערי צדק', verbose_name="שערי צדק")
    הר_הצופים = models.CharField(max_length=512, null=True, blank=True, db_column='הר הצופים', verbose_name="הר הצופים")
    סנט_ג_וזף = models.CharField(max_length=512, null=True, blank=True, db_column="סנט ג'וזף", verbose_name="סנט ג'וזף")
    אסותא = models.CharField(max_length=512, null=True, blank=True, db_column='אסותא')
    ברזילי = models.CharField(max_length=512, null=True, blank=True, db_column='ברזילי')
    סורוקה = models.CharField(max_length=512, null=True, blank=True, db_column='סורוקה')
    יוספטל = models.CharField(max_length=512, null=True, blank=True, db_column='יוספטל')
    הלל_יפה = models.CharField(max_length=512, null=True, blank=True, db_column='הלל יפה')
    העמק = models.CharField(max_length=512, null=True, blank=True,db_column='העמק')
    פוריה = models.CharField(max_length=512, null=True, blank=True, db_column='פוריה')
    זיו = models.CharField(max_length=512, null=True, blank=True, db_column='זיו')
    המרכז_הרפואי_לגליל = models.CharField(max_length=512, null=True, blank=True, db_column='המרכז הרפואי לגליל')
    רמב_ם = models.CharField(max_length=512, null=True, blank=True, db_column='רמב"ם', verbose_name='רמב"ם')
    בני_ציון_רוטשילד = models.CharField(max_length=512, null=True, blank=True, db_column='בני ציון (רוטשילד)', verbose_name="בני ציון (רוטשילד)")
    כרמל = models.CharField(max_length=512, null=True, blank=True, db_column='כרמל')

    class Meta:
        db_table = 'compare'  # Set your custom database table name
        managed = False               # Django can manage this table

    def __str__(self):
        return f"{self.title} - {self.category}"
