from django.db import models
from django.core.exceptions import ValidationError


class IncludeBlock(models.Model):
    template_path = models.CharField(max_length=255,
                                     help_text='Path for {% include %}, ex: web_site/includes/template.html')
    css_class = models.CharField(max_length=255, help_text='That field-content will be put into class="..."',
                                 default='col-lg-4 col-md-4 col-sm-6')
    priority = models.IntegerField(default=0, help_text='The bigger, the better')

    def __unicode__(self):
        return self.template_path

    def clean(self):
        if IncludeBlock.objects.filter(template_path=self.template_path).exclude(pk=self.pk).count() != 0:
            raise ValidationError('Instance with path %s already exists' % self.template_path)
        return super(IncludeBlock, self).clean()