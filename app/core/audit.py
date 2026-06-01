from app.database.models import AuditLog


def log_audit(

    db,

    username,

    action,

    resource,

    details=""
):

    audit = AuditLog(

        username=username,

        action=action,

        resource=resource,

        details=details
    )

    db.add(audit)

    db.commit()