Vim�UnDo� R.�Zd��M��91�iL;�<�\E�  j                                   X�8A    _�                     �       ����                                                                                                                                                                                                                                                                                                                            �          �          v       X�6�     �   �   �                  return self.output(h)�   �   �          !        h = F.relu(self.full0(h))�   �   �                  h = F.relu(h)�   �   �          .        h = F.max_pooling_2d(self.conv2(h), 2)�   �   �                  h = F.relu(h)�   �   �          .        h = F.max_pooling_2d(self.conv1(x), 2)5�_�                    �       ����                                                                                                                                                                                                                                                                                                                            �          �          v       X�7_     �   �   �          E        # # h = bst.bst(self.bn3(self.full0(h), test=not self.train))�   �   �          B        # h = F.relu(self.bn3(self.full0(h), test=not self.train))�   �   �                  # h = F.relu(h)�   �   �                  # # h = bst.bst(h)�   �   �          O        # h = F.max_pooling_2d(self.bn2(self.conv2(h), test=not self.train), 2)�   �   �                  # h = F.relu(h)�   �   �                  # # h = bst.bst(h)�   �   �          O        # h = F.max_pooling_2d(self.bn1(self.conv1(x), test=not self.train), 2)5�_�                    �       ����                                                                                                                                                                                                                                                                                                                            �          �          V       X�7v     �   �   �          9                #bn1    = L.BatchNormalization(n_layer1),5�_�                    �       ����                                                                                                                                                                                                                                                                                                                            �          �          V       X�7w     �   �   �          9                #bn2    = L.BatchNormalization(n_layer2),5�_�                    �       ����                                                                                                                                                                                                                                                                                                                            �          �          V       X�7x     �   �   �          6                #bn3   = L.BatchNormalization(n_full),5�_�                     �       ����                                                                                                                                                                                                                                                                                                                            �          �          V       X�8@    �   �   �                  # return self.output(h)5��