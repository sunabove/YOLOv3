import os, json, cv2, cv2 as cv

def create_label_image( json_file_path, image_folder, image_label_folder, debug=0 ) :
    image_label_path = None
    with open( json_file_path, 'r') as f:
        json_data = json.load( f )

        label_info = json_data['label_info']

        image_file_name = label_info['image']['file_name'] # 이미지 파일명

        image_path = image_folder + image_file_name 

        if not os.path.exists( image_path ) : 
            debug and print( f"image file [{image_file_name}] does not exists." )
        else : 
            image_label_path = image_label_folder + image_file_name.replace( ".jpg", "_label.jpg" )
            
            debug and print( f"image_path = {image_path}" )
            debug and print( f"image_label_path = {image_label_path}" )

            image = cv2.imread( image_path )

            annotations =  label_info['annotations']
            for annot in annotations:
                box = annot['bbox'] # 객체 1개의 bbox 위치 좌표
                cv2.rectangle(image, box[0:2], box[2:], (255,0,0), 2 )
            pass

            cv2.imwrite( image_label_path, image ) 
        pass
    pass

    return image_label_path
pass