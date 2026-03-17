import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Bika_Project.settings')
django.setup()

from bika.models import SiteInfo

def update_tagline():
    site_info = SiteInfo.objects.first()
    if site_info:
        old_tagline = site_info.tagline
        site_info.tagline = "Your inventory Our Innovation"
        site_info.save()
        print(f"Updated SiteInfo tagline from '{old_tagline}' to 'Your inventory Our Innovation'")
    else:
        SiteInfo.objects.create(
            name="Bika",
            tagline="Your inventory Our Innovation",
            description="Your Success Is Our Business - Bika provides exceptional services to help your business grow.",
            email="contact@bika.com",
            phone="+250 798 780 022",
            address="Kigali, Rwanda",
        )
        print("No SiteInfo found. Created default SiteInfo with new tagline.")

if __name__ == "__main__":
    update_tagline()
