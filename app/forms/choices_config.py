# Define the currency choices and codes
CURRENCY_CHOICES = ['USD','EUR','JPY','GBP','AUD','CAD','CHF','CNY','SEK','NZD','MXN','SGD','HKD','NOK','KRW','TRY','INR','RUB','BRL','ZAR',]

# Define the allowed invoice types
INVOICE_TYPES = ['Commercial', 'Pro Forma', 'Consular']

CLEARANCE_CHOICES = [
    ('Port of New York', 'Port of New York'),
    ('Los Angeles International Airport', 'Los Angeles International Airport'),
    ('Singapore Customs Office', 'Singapore Customs Office')
]

# Define the allowed Job types
JOB_TYPES = ['Import', 'Export', 'Domestic']

# Define the allowed contract types
CONTRACT_TYPES=['CIF','FOB']

# Define the allowed payment types
PAYMENT_TYPES=['Advance Payment','Letter of credit']

# Define the allowed Operation handling
OPERATION_HANDLED_BY=['TEAM A','JOHN SMITH']

# Define the allowed POD CHOICES
PORTS_CHOICES=['Port of Singapore','Port of Rotterdam']

CHA_CHOICES=[  # Predefined choices for the SelectField
            ('ABC Customs Services Ltd', 'ABC Customs Services Ltd'),
            ('Global Trade Brokers Inc', 'Global Trade Brokers Inc'),
            ('XYZ Logistics and Customs', 'XYZ Logistics and Customs')
        ]

JOBS=['JOB 12345', 'JOB 7896']

SERIES=['Series A', 'Series B']

EXPORTERS=['EXPORTER A', 'SHIPPER A']

SHIPPING_LINES=['LINE A', 'LINE B']

BL_TYPES=['Master BL','House of BL','Negotiatable BL']

PACKAGE_TYPES=[('BOX','BOX'),('CRT','CRATE'),('PAL','PALLET'),('DRM','DRUM'),('BAG','BAG'),('BAR','BARREL'),('CNT','CONTAINER'),('ROL','ROLL'),('BLK','BULK'),('ENV','ENVELOPE')]

SHIPPING_METHODS=['Standard','Express']

SHIPPING_TYPES=['FCL','LCL','AIR FREIGHT']

UNIT_TYPES=['STANDARD', 'PALLET','BOXES']