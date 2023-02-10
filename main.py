"""

1. GCPにてGoogle Drive APIを有効化
2-1. GCPのメニュー>APIとサービス>認証情報>認証情報を作成 を押下
2-2. サービスアカウント を選択
2-3. サービスアカウントを作成
3-1. アクセスしたいGoogleDriveにフォルダ作成し対象のファイルを格納
3-2. 3-1のフォルダで共有から2-3で作成したサービスアカウントのアドレスを追加
4-1. 2-3で作成したサービスアカウントのkeyファイルをjsonでDL
4-2. ファイル名をcred.jsonにして同ディレクトリに格納
5-1. find_file_listでファイルを確認
5-2. file_idを引数にdownload_fileでDL

"""

from google.oauth2 import service_account
import googleapiclient
from googleapiclient.discovery import build


class GoogleDriver:
    """Operate Google Drive.
    Authentication uses a GCP service account.
    """
    @staticmethod
    def _client() -> googleapiclient.discovery:
        """Create a client for GoogleDriveAPI.

        Returns:
            googleapiclient.discovery: client with SCOPE.
        """
        SCOPES = [
            'https://www.googleapis.com/auth/drive',
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive.readonly"

        ]
        service_account_cred = service_account.Credentials.from_service_account_file("cred.json")
        scoped_creds = service_account_cred.with_scopes(SCOPES)
        return build('drive', 'v3', credentials=scoped_creds)

    def find_file_list(self) -> list:
        """Get a list of available files.

        Returns:
            list: List of files that can be operated. Contains file_id.
        """
        client = self._client()

        results = client.files().list().execute()
        return results["files"]

    def download_file(self, file_id: str) -> any:
        """Get a list of available files.

        Args:
            file_id: file_id of the file to download. You can get it with find_file_list.
        Returns:
            any: bytes format file.
        """
        client = self._client()

        results = client.files().get_media(fileId=file_id).execute()
        return results
