from .models import Appointment


def get_notification(request):
    """
    Function that count new appointments and clear them when they are accepted
    """
    count = Appointment.objects.filter(accepted=False).count()
    data = {
        "count": count
    }
    return data
