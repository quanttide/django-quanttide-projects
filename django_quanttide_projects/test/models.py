from django_quanttide.test import ModelTestCase

from django_quanttide_projects.models import BaseProject


class ProjectModelTestCase(ModelTestCase):
    model_class: BaseProject = BaseProject
    model_data: dict = {}

    def test_defaults(self):
        model_instance: BaseProject = super().test_defaults()
        # Test verbose_name field
        self.assertEqual(model_instance.verbose_name, self.model_data['verbose_name'])
        # Test created_at field
        self.assertIsNotNone(model_instance.created_at)
        # Test updated_at field
        previous_updated_at = model_instance.updated_at
        model_instance.save()
        self.assertGreater(model_instance.updated_at, previous_updated_at)
