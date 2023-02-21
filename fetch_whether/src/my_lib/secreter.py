from google.cloud import secretmanager, exceptions as exc, logging
from retry import retry
import os


@retry(Exception, tries=3, delay=2)
def get_secret(project_id: str, secret_id: str, version='latest') -> any:
    """Get secret from SecretManager.

    Args:
        project_id (str): GCP ProjectId.
        secret_id (str): SecretID set in Secret Manager.
        version (str): Secret Version. Default value is latest.

    Returns:
        any: The value associated with secret_id.

    Raises:
        NotFound: secret_id does not exist or is incorrect.
        Exception: Some Error Occurred.
    """
    name = f"projects/{project_id}/secrets/{secret_id}/versions/{version}"
    client = secretmanager.SecretManagerServiceClient()

    try:
        res = client.access_secret_version(request={"name": name}).payload.data.decode("UTF-8")
        return res
    except exc.NotFound:
        raise _send_log("Failed to get secret.", f"Secret {secret_id} was not found.", "ERROR")
    except Exception as err:
        _send_log("Some Error Occurred so Retrying...", str(err), "WARNING")
        raise _send_log("Some Error Occurred.", str(err), "ERROR")


def _send_log(overview: str, details: str, severity: str):
    """Send log to CloudLogging.

    Args:
        overview (str): Describe the log summary.
        details (str): Describe the log details.
        severity (str): Select NOTICE/WARNING/ERROR.
    """
    client = logging.Client()
    client.setup_logging()
    logger = client.logger(os.getenv("FUNCTION_TARGET", default="local"))

    logger.log_struct(
        {
            "severity": severity,
            "message": overview,
            "details": details,
        },
    )
