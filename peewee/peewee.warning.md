    def get_or_create(self, *filter, **kwargs):
        try:
            return self.model.get(*filter)
        except self.model.DoesNotExist:
            my_item = self.model.create(**kwargs)  # just return kwargs, other set None
            return self.model.get(self.model.id==my_item.id)
