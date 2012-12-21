from StringIO import StringIO
from django.core.serializers.python import Serializer as BaseSerializer, Deserializer
from django.utils.encoding import smart_unicode

class Serializer(BaseSerializer):
    def handle_fk_field(self, obj, field):
        self._current[field.name] = smart_unicode(field._get_val_from_obj(obj), strings_only=True)

    def serialize(self, queryset, **options):
        """
        Serialize a queryset.
        """
        self.options = options

        self.stream = options.get("stream", StringIO())
        self.selected_fields = options.get("fields")
        self.use_natural_keys = options.get("use_natural_keys", False)

        self.start_serialization()
        for obj in queryset:
            self.start_object(obj)
            fields = getattr(obj, 'all_fields', obj._meta.local_fields)
            for field in fields:
                if field.serialize:
                    if field.rel is None:
                        if self.selected_fields is None or field.attname in self.selected_fields:
                            self.handle_field(obj, field)
                    else:
                        if self.selected_fields is None or field.attname[:-3] in self.selected_fields:
                            self.handle_fk_field(obj, field)
            for field in obj._meta.many_to_many:
                if field.serialize:
                    if self.selected_fields is None or field.attname in self.selected_fields:
                        self.handle_m2m_field(obj, field)
            self.end_object(obj)
        self.end_serialization()
        return self.getvalue()

    def start_object(self, obj):
        self._current = {}
        for parent in obj._meta.parents.values():
            if parent:
                parent_obj = getattr(obj, parent.name, None)
                obj.all_fields = obj._meta.local_fields + parent_obj._meta.local_fields
                
