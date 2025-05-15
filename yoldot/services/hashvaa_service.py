from ..models import Hashvaa
from ..serializers import HashvaaSerializer
from collections import defaultdict

def get_all_hashvaot():
    """Get all hashvaot and group by category."""
    hashvaot = Hashvaa.objects.all()
    serialized_data = HashvaaSerializer(hashvaot, many=True).data
    
    # Group by category
    data = defaultdict(list)
    for item in serialized_data:
        category = item.get('category')
        if category:
            data[category].append(item)
    
    # Convert defaultdict to a regular dict
    return dict(data)
