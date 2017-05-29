from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from core.factories import IndicatorReportFactory
# from indicator.models import IndicatorReport
from unicef.models import ProgrammeDocument
from indicator.models import IndicatorReport
from account.models import User


class TestPDReportsAPIView(APITestCase):

    def setUp(self):
        # By calling this factory, we're creating
        # IndicatorReport -> Reportable -> LowerLevelOutput -> CountryProgrammeOutput -> ProgrammeDocument
        IndicatorReportFactory.create_batch(5)

        # Make all requests in the context of a logged in session.
        admin, created = User.objects.get_or_create(username='admin', defaults={
            'email': 'admin@unicef.org',
            'is_superuser': True,
            'is_staff': True
        })
        admin.set_password('Passw0rd!')
        admin.save()
        self.client = APIClient()
        self.client.login(username='admin', password='Passw0rd!')

    def test_list_api(self):
        pd = ProgrammeDocument.objects.first()
        url = reverse('programme-document-reports', kwargs={'pd_id': pd.pk})
        response = self.client.get(url, format='json')

        self.assertTrue(status.is_success(response.status_code))

        pd = ProgrammeDocument.objects.get(pk=pd.id)
        pks = pd.reportable_queryset.values_list('indicator_reports__pk', flat=True)
        count = IndicatorReport.objects.filter(id__in=pks).count()

        self.assertEquals(len(response.data), count)
