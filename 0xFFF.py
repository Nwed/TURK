3
���^U  �               @   s$  d dl Z d dlmZ d dlZdd� Zed�Zed� edk�r�ed�Z	d	e	 Z
e je
�jZd
ZdZeeje�ee� eje�� ZdZdZeeje�ee� eje�� ZdZdZeeje�ee� eje�� ZdZdZeeje�ee� eje�� Zeed�Zejdddid�Zejd�ZdZ dZ!eeje �ee � eje!�� Z"dZ#dZ$eeje#�ee#� eje$�� j%dd�Z&dZ'dZ(eeje'�ee'� eje(�� Z)d Z*d!Z+eeje*�ee*� eje+�� Z,d"Z-d#Z.eeje-�ee-� eje.�� Z/ed$e� �� ed%e� �� ed&e� �� ed'e� �� ed(e� �� d)e"k�rRed*e"j%d+d�� e&d,k�rfed-� ned.e&� �� e)d/k�r�ed0� ned1� e,d/k�r�ed2� ned3� e/d/k�r�ed4� ned5� e0�  ed6k�r�e1ed7��Z2d8e2 d9 Z3d:Z4d;Z5e3d<d=�Z6e j7e5d>e4ie6d?�Z8ee8j� dS )@�    N)�BeautifulSoupc              C   sF   d} d}d}d}d}d}d}t j� }||jd< ||jd	< ||jd
< d S )Nz[0mz[1;31mz[1;32mz[1;36mz[1;33mziMozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36zen-US,en;q=0.5z
User-AgentzAccept-LanguagezContent-Language)�requests�Session�headers)�nu�reZgr�cyZylZ
USER_AGENT�LANGUAGE�session� r   �0xFFF.py�
instascrap   s    

r   u�  
    
    ------------------------------------------
    0xFFF معلومات             
    snapchat: flaah999       
    ------------------------------------------
    

الان تستطيع جلب معلومات 
عن المستخدم في الاستقرام 🐺
 
    1 - اظهار البيانات الخاصه مثل الاميل ..
    2 - اظهار بيانات صفحته علي الاستقرام
    
    
    u$   
برمجة : فلاح العنزي
�2zEnter Username: zhttps://www.instagram.com/z"full_name":"z","has_ar_effects"z"id":"z","is_business_account"z"edge_followed_by":{"count":z},"followed_by_viewer"z"edge_follow":{"count":z},"follows_viewer"zhtml.parser�meta�propertyzog:image)�attrs�contentz"external_url":z,"external_urlz"biography":"z","blocked_by_viewer"z\n� zis_private":z,"is_verified"z"is_verified":z,"edge_mutual_followed_by"z"is_business_account":z,"is_joined_recently"zName: zID: zFollowers: zFollowing: zProfile Pic:z""zExternal URL:�"� zBiography: NonezBiography: �falsezPrivate Account: NozPrivate Account: YeszVerified Account: NozVerified Account: YeszBusiness Account: NozBusiness Account: Yes�1zEnter User: zG35a2d547d3b6ff400f713948cdffe0b789a903f86117eb6e2f3e573079b2f038.{"q":"zO","guid":"b449de3c-1663-47bc-8cca-e83b570b60d1","device_id":"615d8b7997acf12b"}zInstagram 99.4.0z,https://i.instagram.com/api/v1/users/lookup/�9)Zsigned_bodyZig_sig_key_versionz
User-Agent)r   �data)9r   �bs4r   �urllib.parse�urllibr   �input�op�printZinstaUsernameZinstaURL�get�textZinstaURLReqZstartsWithURLZendsWithURL�find�len�rfindZinstaWithURLZstartsWithIDZ
endsWithIDZinstaWithIDZstartsWithFollowedZendsWithFollowedZinstaFollowersZstartsWithFollowingZendsWithFollowingZinstaFollowingZ	instaSoupZinstaPPZinstaProfilePicZstartsWithExternalLinkZendsWithExternalLinkZinstaExternalLinkZstartsWithBiographyZendsWithBiography�replaceZinstaBiographyZstartWithPrivateZendsWithPrivateZinstaIsPrivateZstartWithVerifiedZendsWithVerifiedZinstaIsVerifiedZstartWithBusinessZendsWithBusinessZinstaBusiness�exit�str�user�sZ
userAAgent�urlZmyobj�post�xr   r   r   r   �<module>   s�   
    

 (   










