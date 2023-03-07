
class AddClassMixin:
  def add_classes(self, classes: list[str]) -> None:
    for field in self.fields.values():
      field.widget.attrs.update({'class': ' '.join(classes)})
