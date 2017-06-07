from rest_framework import serializers

from .models import ProgrammeDocument, Section


class ProgrammeDocumentSerializer(serializers.ModelSerializer):

    status = serializers.CharField(source='get_status_display')
    total_unicef_supplies = serializers.SerializerMethodField()

    class Meta:
        model = ProgrammeDocument
        fields = (
            'id',
            'agreement',
            'reference_number',
            'title',
            'unicef_office',
            'unicef_focal_point',
            'partner_focal_point',
            'start_date',
            'end_date',
            'population_focus',
            'response_to_HRP',
            'status',
            'calculated_budget',
            'cso_contribution',
            'unicef_cash',
            'total_unicef_supplies',
        )

    def get_total_unicef_supplies(self, obj):
        return str(obj.in_kind_amount)


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ('name', )


class ProgrammeDocumentDetailSerializer(serializers.ModelSerializer):

    document_type = serializers.CharField(source='get_document_type_display')
    # status is choice field on different branch with migration #23 - should be uncomment when it will be merged
    # status = serializers.CharField(source='get_status_display')
    frequency = serializers.CharField(source='get_frequency_display')
    # sections = serializers.SerializerMethodField()
    sections = SectionSerializer(read_only=True, many=True)

    class Meta:
        model = ProgrammeDocument
        fields = (
            'id',
            'agreement',
            'document_type',
            'reference_number',
            'title',
            'unicef_office',
            'unicef_focal_point',
            'partner_focal_point',
            'response_to_HRP',
            'start_date',
            'end_date',
            'population_focus',
            # 'status',
            'frequency',
            'sections',
        )
