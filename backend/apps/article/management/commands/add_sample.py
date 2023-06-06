from django.core.management.base import BaseCommand
from article.models.article import Article

samples = [
    {
        "title": "Nulla facilisi",
        "content": "Nulla facilisi. Ut rutrum faucibus purus, vel commodo tellus lobortis id. Mauris non augue in nisl cursus malesuada. Ut eu interdum ipsum, ut pellentesque purus. Proin ex felis, consectetur non odio a, congue consectetur nisi. In eleifend quam odio, vel feugiat dolor finibus sed. Suspendisse porta mauris sed molestie feugiat."
    },
    {
        "title": "Proin condimentum",
        "content": "Nulla facilisi. Proin condimentum nisl nec aliquam commodo. Fusce in purus ut quam blandit interdum. Vestibulum eleifend eleifend augue. Morbi porta eros sapien, non tempor dolor feugiat id. Curabitur elementum est nisl. Donec rhoncus lectus metus, nec porttitor odio ullamcorper vitae. Curabitur sollicitudin mattis magna. Maecenas lacus mauris, consequat viverra sagittis volutpat, volutpat ut dui. Fusce felis elit, egestas sit amet velit a, suscipit cursus nulla. Donec interdum, diam quis iaculis tristique, lorem erat tristique massa, at venenatis turpis sem eget mi. Vivamus id elit orci."
    },
    {
        "title": "Etiam eget hendrerit mi",
        "content": "Etiam eget hendrerit mi. Aliquam erat volutpat. Suspendisse posuere hendrerit pretium. Etiam quis fringilla arcu. Nam ac fringilla est. In congue sodales lacus, ullamcorper semper enim vehicula ut. Praesent magna velit, fringilla ut finibus quis, euismod in turpis. Duis quis velit efficitur, sodales ex ac, ornare risus. Vestibulum eu aliquet mi, eget pharetra quam. Suspendisse sed sapien in erat tristique semper. Sed accumsan odio non mauris vulputate scelerisque. Praesent vitae luctus justo. Aliquam erat volutpat. Duis tempor iaculis metus, a bibendum augue vehicula quis. Curabitur et volutpat lacus."
    },
    {
        "title": "Phasellus quam tortor",
        "content": "Phasellus quam tortor, aliquet id efficitur a, faucibus ullamcorper metus. Praesent commodo eget nisl quis interdum. Nullam lobortis egestas ipsum a varius. Donec eu scelerisque odio. Proin ac ornare quam. In tempus viverra scelerisque. Maecenas quam lorem, rutrum sed pellentesque sed, ultricies vitae nunc. Pellentesque tincidunt elit nulla, eget hendrerit tellus cursus varius. Suspendisse suscipit lacinia est ultricies imperdiet. Curabitur eget dictum nisl, at laoreet nisi."
    },
    {
        "title": "Sed iaculis",
        "content": "Sed iaculis, ex ac posuere tincidunt, diam tortor venenatis risus, vitae dictum metus quam ac ex. Praesent in mauris elit. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Sed vitae pulvinar lorem. Mauris dictum ultrices ultricies. Fusce congue est eu turpis rutrum tincidunt. Proin eget gravida augue. Phasellus feugiat tincidunt vulputate. Mauris hendrerit pharetra euismod. Fusce pretium magna nec nisi vulputate porttitor. Cras dictum odio sed velit porta, sed facilisis nulla luctus. Aenean nec ligula ut metus eleifend bibendum sed ac nunc."
    }
]

class Command(BaseCommand):
    def handle(self, *args, **options):
        for sample in samples:
            article = Article()
            article.title = sample["title"]
            article.content = sample["content"]
            article.save()