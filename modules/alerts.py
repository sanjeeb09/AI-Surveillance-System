from plyer import notification


def send_alert(people, fusion_score):

    notification.notify(
        title="🚨 Suspicious Activity Detected"
        message=(
            f"AI Surveillance System\n\n"
            f"People Detected: {people}\n"
            f"Fusion Score : {fusion_score:.2f}\n\n"
            f"Automatic recording has started."
        ),
        timeout=8
    )