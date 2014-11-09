/*


 */

#ifndef __DATAITERATOR_H__
#define __DATAITERATOR_H__

class DataIterator {
public:
  /// Constructor. This would set ranges. Could depend on thread number
  DataIterator(int xs, int xe,
               int ys, int ye,
               int zs, int ze) : x(xs), y(ys), z(zs), 
                                 xstart(xs), xend(xe), 
                                 ystart(ys), yend(ye),
                                 zstart(xs), zend(ze) {
  }
  
  /// The index variables, updated during loop
  int x, y, z;

  /// Increment operators
  DataIterator& operator++() { next(); return *this; }
  DataIterator& operator++(int) { next(); return *this; }

  void start() {
    x = xstart; y = ystart; z = zstart;
  }
  
  /// Checks if finished looping. Is this more efficient than
  /// using the more idiomatic it != MeshIterator::end() ?
  bool done() const {
    return x > xend;
  }
  
private:
  DataIterator(); // Disable null constructor
  
  int xstart, xend;
  int ystart, yend;
  int zstart, zend;
  
  /// Advance to the next index
  void next() {
    z++;
    if(z > zend) {
      z = zstart;
      y++;
      if(y > yend) {
        y = ystart;
        x++;
      }
    }
  }
};

/*
template<>
struct DataIterable {
  DataIterable();
}
*/

#endif // __DATAITERATOR_H__