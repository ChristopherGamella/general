from services.database_service import DatabaseService
from services.http_service import HttpService
from services.elasticsearch_service import ElasticsearchService
from services.notification_service import NotificationService
from utils.config import Config

def main():
    config = Config()
    
    db_service = DatabaseService(config)
    http_service = HttpService(config)
    es_service = ElasticsearchService(config)
    notification_service = NotificationService(config)
    
    # Example usage
    db_service.connect()
    http_service.make_request()
    es_service.index_data()
    notification_service.send_email()

if __name__ == "__main__":
    main()