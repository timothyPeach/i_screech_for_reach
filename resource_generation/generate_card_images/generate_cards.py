from PIL import Image, ImageDraw, ImageFont
import custom_geo
import tupleize
import json

with open("card_definitions.json") as cdef_file:
    cdef = json.load(cdef_file)
cdef = tupleize.tupleize(cdef)

number_of_cards = len(cdef['cards'])
total_size = (cdef['dimensions']['size'][0]*number_of_cards,cdef['dimensions']['size'][1])

card_stock = Image.open(cdef['card_stock']['file'])
card_stock = card_stock.crop(cdef['card_stock']['crop_offset']+cdef['dimensions']['size'])

opaque = (0,0,0,255)
card_cutout = custom_geo.gen_rounded_rectangle(cdef['dimensions']['size'],cdef['dimensions']['corner_round_radius'],'RGBA',opaque)

bg_image = Image.new('RGBA',cdef['dimensions']['size'],cdef['bg_color'])

for suit in cdef['suits'].keys():
        card_sheet_image = Image.new('RGBA',total_size,cdef['bg_color'])
        pip_image = Image.open(cdef['suits'][suit]['pip'])
        
        for card_index,card in enumerate(cdef['cards'].keys()):
            card_image = card_stock.copy()
            
            if cdef['cards'][card]['is_face']:
                face_image = Image.open(cdef['suits'][suit]['faces'][card]['image'])
                card_image.paste(face_image,box=(0,0),mask=face_image)
            else:#pip based image
                effective_locations = []
                for location in cdef['cards'][card]['pips']:
                    effective_locations.append(location)
                for mirror in cdef['cards'][card]['mirrors']:
                    new_locations = []
                    for location in effective_locations:
                        center_anchored_location = custom_geo.center_anchor(location,(1,1))
                        center_anchored_mirrored_location = custom_geo.mirror(center_anchored_location,mirror)
                        mirrored_location = custom_geo.center_unanchor(center_anchored_mirrored_location,(1,1))
                        if not custom_geo.too_close(location,mirrored_location,0.01):
                            new_locations.append(mirrored_location)
                    effective_locations.extend(new_locations)
                for location in effective_locations:
                    location_scaled = custom_geo.center_anchor(custom_geo.relative_location(location,card_image.size),pip_image.size)
                    location_scaled_int = custom_geo.makeint(location_scaled)
                    card_image.paste(pip_image,box=location_scaled_int,mask=pip_image)
                    
            finished_card_image = Image.composite(card_image,bg_image,card_cutout)
            location_in_sheet = (card_index*card_stock.size[0],0)
            card_sheet_image.paste(finished_card_image,box=location_in_sheet,mask=finished_card_image)
        card_sheet_image.show()














