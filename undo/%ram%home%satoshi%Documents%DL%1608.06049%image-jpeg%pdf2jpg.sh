Vim�UnDo� pf�������c6��:�^���r!����H6|              echo "$pdf Done."                             Y���    _�                             ����                                                                                                                                                                                                                                                                                                                                                             Y���     �                   �               5�_�      
                     ����                                                                                                                                                                                                                                                                                                                                                             Y��    �               for i in *.md5�_�                
          ����                                                                                                                                                                                                                                                                                                                                                             Y��P     �                   pdf="${param}.pdf"5�_�   
                        ����                                                                                                                                                                                                                                                                                                                                                             Y��T    �                   jpg="${param}.pdf"5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Y��Z    �      	             if [ -f $pdf ]; then5�_�                    	       ����                                                                                                                                                                                                                                                                                                                                                             Y��^    �      
         !        echo "$pdf alredy exist."5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Y��c     �   
                    pandocpdf -o $pdf $i5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Y��n     �   
                    convert -o $pdf $i5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Y��z     �   
                    convert $pdf $i5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Y���     �   
                    convert $jpg $i5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Y���    �   
                    convert $jpg $jpg5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Y���    �                       echo "$pdf Done."5�_�             
             ����                                                                                                                                                                                                                                                                                                                                                             Y��     �              5�_�                          ����                                                                                                                                                                                                                                                                                                                                                             Y��'     �                   pdf="${i}.pdf"5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Y��*     �                   jpg="${i}.pdf"5�_�      	                     ����                                                                                                                                                                                                                                                                                                                                                             Y��.     �                   jpg="${i}.jpg"5�_�                  	          ����                                                                                                                                                                                                                                                                                                                                                             Y��1    �                   if [ -f $jpg ]; then5�_�                          ����                                                                                                                                                                                                                                                                                                                                                             Y��"     �                   if [ -f $ ]; then5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Y��     �              5��