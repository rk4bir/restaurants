from accounts.models import Account
#from notifications.models import Notification


def account_processor(request):
	try:
		ACCOUNT = Account.objects.get(user=request.user)
	except:
		ACCOUNT = None
	return {'ACCOUNT': ACCOUNT}

def notification_processor(request):
	N_UNSEEN = 0
	NOTIFICATIONS = None
	if request.user.is_authenticated:
		try:
			NOTIFICATIONS   = Notification.objects.all().filter(account=Account.objects.get(user=request.user))
			N_UNSEEN = NOTIFICATIONS.filter(is_seen=False).count
		except:
			pass
	return {'NOTIFICATIONS': NOTIFICATIONS, 'UNSEEN': N_UNSEEN}
