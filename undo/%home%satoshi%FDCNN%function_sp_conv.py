Vim�UnDo� Z����[�Ø�������:��8�����  �           W_f = ifftshift(W_f)   M                          Y#,�    _�                     K       ����                                                                                                                                                                                                                                                                                                                                                             Y>�     �   J   L  �              W_f = fftshift(W_f)5�_�                    M       ����                                                                                                                                                                                                                                                                                                                                                             Y>�    �   L   N  �              W_f = ifftshift(W_f)5�_�                    �        ����                                                                                                                                                                                                                                                                                                                            �          �           V        Y#,�     �   �   �           �   �   �                  gy_f = fft2(gy_ex)�   �   �          X        gy_ex[:,:,0:gyh,0:gyw] = numpy.rot90(gy,2,(2,3)) #require numpy version >= v1.12�   �   �          @        gy_ex = numpy.zeros((gyn,gyc,h,w),dtype=numpy.complex64)5�_�                     Q       ����                                                                                                                                                                                                                                                                                                                            Q          Q          V       Y#,�    �   P   R                  x_f = fft2(x)5��