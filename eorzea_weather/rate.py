from .zone import Zones

rates = {
    Zones.LIMSA_LOMINSA: {
        '20': 'Clouds',
        '50': 'Clear Skies',
        '80': 'Fair Skies',
        '90': 'Fog',
        '100': 'Rain'
    },
    Zones.MIDDLE_LA_NOSCEA: {
        '20': 'Clouds',
        '50': 'Clear Skies',
        '70': 'Fair Skies',
        '80': 'Wind',
        '90': 'Fog',
        '100': 'Rain'
    },
    Zones.LOWER_LA_NOSCEA: {
        '20': 'Clouds',
        '50': 'Clear Skies',
        '70': 'Fair Skies',
        '80': 'Wind',
        '90': 'Fog',
        '100': 'Rain'
    },
    Zones.EASTERN_LA_NOSCEA: {
        '5': 'Fog',
        '50': 'Clear Skies',
        '80': 'Fair Skies',
        '90': 'Clouds',
        '95': 'Rain',
        '100': 'Showers'
    },
    Zones.WESTERN_LA_NOSCEA: {
        '10': 'Fog',
        '40': 'Clear Skies',
        '60': 'Fair Skies',
        '80': 'Clouds',
        '90': 'Wind',
        '100': 'Gales'
    },
    Zones.UPPER_LA_NOSCEA: {
        '30': 'Clear Skies',
        '50': 'Fair Skies',
        '70': 'Clouds',
        '80': 'Fog',
        '90': 'Thunder',
        '100': 'Thunderstorms'
    },
    Zones.OUTER_LA_NOSCEA: {
        '30': 'Clear Skies',
        '50': 'Fair Skies',
        '70': 'Clouds',
        '85': 'Fog',
        '100': 'Rain'
    },
    Zones.THE_MIST: {
        '20': 'Clouds',
        '50': 'Clear Skies',
        '70': 'Fair Skies',
        '80': 'Fair Skies',
        '90': 'Fog',
        '100': 'Rain'
    },
    Zones.GRIDANIA: {
        '5': 'Rain',
        '20': 'Rain',
        '30': 'Fog',
        '40': 'Clouds',
        '55': 'Fair Skies',
        '85': 'Clear Skies',
        '100': 'Fair Skies'
    },
    Zones.CENTRAL_SHROUD: {
        '5': 'Thunder',
        '20': 'Rain',
        '30': 'Fog',
        '40': 'Clouds',
        '55': 'Fair Skies',
        '85': 'Clear Skies',
        '100': 'Fair Skies'
    },
    Zones.EAST_SHROUD: {
        '5': 'Thunder',
        '20': 'Rain',
        '30': 'Fog',
        '40': 'Clouds',
        '55': 'Fair Skies',
        '85': 'Clear Skies',
        '100': 'Fair Skies'
    },
    Zones.SOUTH_SHROUD: {
        '5': 'Fog',
        '10': 'Thunderstorms',
        '25': 'Thunder',
        '30': 'Fog',
        '40': 'Clouds',
        '70': 'Fair Skies',
        '100': 'Clear Skies'
    },
    Zones.NORTH_SHROUD: {
        '5': 'Fog',
        '10': 'Showers',
        '25': 'Rain',
        '30': 'Fog',
        '40': 'Clouds',
        '70': 'Fair Skies',
        '100': 'Clear Skies'
    },
    Zones.THE_LAVENDER_BEDS: {
        '5': 'Clouds',
        '20': 'Rain',
        '30': 'Fog',
        '40': 'Clouds',
        '55': 'Fair Skies',
        '85': 'Clear Skies',
        '100': 'Fair Skies'
    },
    Zones.ULDAH: {
        '40': 'Clear Skies',
        '60': 'Fair Skies',
        '85': 'Clouds',
        '95': 'Fog',
        '100': 'Rain'
    },
    Zones.WESTERN_THANALAN: {
        '40': 'Clear Skies',
        '60': 'Fair Skies',
        '85': 'Clouds',
        '95': 'Fog',
        '100': 'Rain'
    },
    Zones.CENTRAL_THANALAN: {
        '15': 'Dust Storms',
        '55': 'Clear Skies',
        '75': 'Fair Skies',
        '85': 'Clouds',
        '95': 'Fog',
        '100': 'Rain'
    },
    Zones.EASTERN_THANALAN: {
        '40': 'Clear Skies',
        '60': 'Fair Skies',
        '70': 'Clouds',
        '80': 'Fog',
        '85': 'Rain',
        '100': 'Showers'
    },
    Zones.SOUTHERN_THANALAN: {
        '20': 'Heat Waves',
        '60': 'Clear Skies',
        '80': 'Fair Skies',
        '90': 'Clouds',
        '100': 'Fog'
    },
    Zones.NORTHERN_THANALAN: {
        '5': 'Clear Skies',
        '20': 'Fair Skies',
        '50': 'Clouds',
        '100': 'Fog'
    },
    Zones.THE_GOBLET: {
        '40': 'Clear Skies',
        '60': 'Fair Skies',
        '85': 'Clouds',
        '95': 'Fog',
        '100': 'Rain'
    },
    Zones.ISHGARD: {
        '60': 'Snow',
        '70': 'Fair Skies',
        '75': 'Clear Skies',
        '90': 'Clouds',
        '100': 'Fog'
    },
    Zones.COERTHAS_CENTRAL_HIGHLANDS: {
        '20': 'Blizzards',
        '60': 'Snow',
        '70': 'Fair Skies',
        '75': 'Clear Skies',
        '90': 'Clouds',
        '100': 'Fog'
    },
    Zones.COERTHAS_WESTERN_HIGHLANDS: {
        '20': 'Blizzards',
        '60': 'Snow',
        '70': 'Fair Skies',
        '75': 'Clear Skies',
        '90': 'Clouds',
        '100': 'Fog'
    },
    Zones.THE_SEA_OF_CLOUDS: {
        '30': 'Clear Skies',
        '60': 'Fair Skies',
        '70': 'Clouds',
        '80': 'Fog',
        '90': 'Wind',
        '100': 'Umbral Wind'
    },
    Zones.AZYS_LLA: {
        '35': 'Fair Skies',
        '70': 'Clouds',
        '100': 'Thunder'
    },
    Zones.THE_DIADEM: {
        '30': 'Fair Skies',
        '60': 'Fog',
        '90': 'Wind',
        '100': 'Umbral Wind'
    },
    Zones.IDYLLSHIRE: {
        '10': 'Clouds',
        '20': 'Fog',
        '30': 'Rain',
        '40': 'Showers',
        '70': 'Clear Skies',
        '100': 'Fair Skies'
    },
    Zones.THE_DRAVANIAN_FORELANDS: {
        '10': 'Clouds',
        '20': 'Fog',
        '30': 'Thunder',
        '40': 'Dust Storms',
        '70': 'Clear Skies',
        '100': 'Fair Skies'
    },
    Zones.THE_DRAVANIAN_HINTERLANDS: {
        '10': 'Clouds',
        '20': 'Fog',
        '30': 'Rain',
        '40': 'Showers',
        '70': 'Clear Skies',
        '100': 'Fair Skies'
    },
    Zones.THE_CHURNING_MISTS: {
        '10': 'Clouds',
        '20': 'Gales',
        '40': 'Umbral Static',
        '70': 'Clear Skies',
        '100': 'Fair Skies'
    },
    Zones.MOR_DHONA: {
        '15': 'Clouds',
        '30': 'Fog',
        '60': 'Gloom',
        '75': 'Clear Skies',
        '100': 'Fair Skies'
    },
    Zones.RHALGRS_REACH: {
        '15': 'Clear Skies',
        '60': 'Fair Skies',
        '80': 'Clouds',
        '90': 'Fog',
        '100': 'Thunder'
    },
    Zones.THE_FRINGES: {
        '15': 'Clear Skies',
        '60': 'Fair Skies',
        '80': 'Clouds',
        '90': 'Fog',
        '100': 'Thunder'
    },
    Zones.THE_PEAKS: {
        '10': 'Clear Skies',
        '60': 'Fair Skies',
        '75': 'Clouds',
        '85': 'Fog',
        '95': 'Wind',
        '100': 'Dust Storms'
    },
    Zones.THE_LOCHS: {
        '20': 'Clear Skies',
        '60': 'Fair Skies',
        '80': 'Clouds',
        '90': 'Fog',
        '100': 'Thunderstorms'
    },
    Zones.KUGANE: {
        '10': 'Rain',
        '20': 'Fog',
        '40': 'Clouds',
        '80': 'Fair Skies',
        '100': 'Clear Skies'
    },
    Zones.SHIROGANE: {
        '10': 'Rain',
        '20': 'Fog',
        '40': 'Clouds',
        '80': 'Fair Skies',
        '100': 'Clear Skies'
    },
    Zones.THE_RUBY_SEA: {
        '10': 'Thunder',
        '20': 'Wind',
        '35': 'Clouds',
        '75': 'Fair Skies',
        '100': 'Clear Skies'
    },
    Zones.YANXIA: {
        '5': 'Showers',
        '15': 'Rain',
        '25': 'Fog',
        '40': 'Clouds',
        '80': 'Fair Skies',
        '100': 'Clear Skies'
    },
    Zones.THE_AZIM_STEPPE: {
        '5': 'Gales',
        '10': 'Wind',
        '17': 'Rain',
        '25': 'Fog',
        '35': 'Clouds',
        '75': 'Fair Skies',
        '100': 'Clear Skies'
    },
    Zones.EUREKA_ANEMOS: {
        '30': 'Fair Skies',
        '60': 'Gales',
        '90': 'Showers',
        '100': 'Snow'
    },
    Zones.EUREKA_PAGOS: {
        '10': 'Clear Skies',
        '28': 'Fog',
        '46': 'Heat Waves',
        '64': 'Snow',
        '82': 'Thunder',
        '100': 'Blizzards'
    },
    Zones.EUREKA_PYROS: {
        '10': 'Fair Skies',
        '28': 'Heat Waves',
        '46': 'Thunder',
        '64': 'Blizzards',
        '82': 'Umbral Wind',
        '100': 'Snow'
    }
}
